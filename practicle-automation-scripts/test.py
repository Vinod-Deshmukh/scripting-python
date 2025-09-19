# import requests
# import json

# url = "https://open.er-api.com/v6/latest/INR"

# try:
#     response = requests.get(url, timeout=10)  # timeout prevents hanging
#     print("Status Code:", response.status_code)

#     data = response.json()
#     print("🌍 Pretty Response:")
#     print(json.dumps(data, indent=4))

#     usd = data["rates"]["USD"]
#     eur = data["rates"]["EUR"]

#     print("1 INR =", usd, "USD")
#     print("1 INR =", eur, "EUR")

# except Exception as e:
#     print("⚠️ Error:", e)

# currency_ui.py
import threading
import requests
import json
import tkinter as tk
from tkinter import ttk, messagebox

# Globals to hold latest rates
RATES = {}
BASE = None
RATES_LOADED = False

# --- Fetch rates (robust) ---
def fetch_rates_from_api():
    """
    Try a reliable public endpoint and normalize the response to:
      - return base_currency (string)
      - return rates (dict) where rates[cur] = number meaning 1 <base> = rates[cur]
    """
    candidates = [
        "https://open.er-api.com/v6/latest/USD",
        "https://open.er-api.com/v6/latest/INR",
        "https://api.exchangerate.host/latest"   # fallback (may require key depending on provider)
    ]
    for url in candidates:
        try:
            r = requests.get(url, timeout=8)
            data = r.json()
            # Debug (uncomment if you want console output)
            # print("DEBUG API:", url)
            # print(json.dumps(data, indent=2))

            # open.er-api returns 'result' or 'result'/'base_code' and 'rates'
            if isinstance(data, dict):
                # Rates might be under 'rates' or 'conversion_rates'
                rates = None
                if "rates" in data and isinstance(data["rates"], dict):
                    rates = data["rates"]
                elif "conversion_rates" in data and isinstance(data["conversion_rates"], dict):
                    rates = data["conversion_rates"]

                # Determine base currency key
                base = data.get("base_code") or data.get("base") or data.get("baseCurrency") or None

                # If rates found, normalize and return
                if rates:
                    # If base isn't provided but the endpoint used USD by default we assume USD
                    if not base:
                        # try to infer typical defaults
                        base = "USD"
                    return base, rates
        except Exception:
            # try next candidate
            continue

    # If all failed raise so the caller can handle fallback
    raise RuntimeError("All rate API attempts failed")


def load_rates_background(on_done=None):
    """Run network fetch in background and then call on_done(base, rates) in main thread."""
    def worker():
        global RATES, BASE, RATES_LOADED
        try:
            base, rates = fetch_rates_from_api()
            # Ensure base included in rates with value 1.0 for easier math
            rates = dict(rates)  # copy
            if base not in rates:
                rates[base] = 1.0
            RATES = rates
            BASE = base
            RATES_LOADED = True
            if on_done:
                root.after(0, on_done, base, rates)
        except Exception as e:
            RATES = {}
            BASE = None
            RATES_LOADED = False
            if on_done:
                root.after(0, on_done, None, None, str(e))

    threading.Thread(target=worker, daemon=True).start()


# --- Conversion logic ---
def convert_amount(amount, from_cur, to_cur):
    """
    Convert amount in from_cur to to_cur using a rates dict where:
       rates[c] means 1 BASE = rates[c].
    Formula:
       amount_in_base = amount / rates[from_cur]   (unless from_cur == base)
       result = amount_in_base * rates[to_cur]     (unless to_cur == base)
    This works for any API base.
    """
    if not RATES_LOADED:
        raise RuntimeError("Rates not loaded")

    # if currency not available in rates, error
    if from_cur not in RATES:
        raise KeyError(f"Rate for {from_cur} not available")
    if to_cur not in RATES:
        raise KeyError(f"Rate for {to_cur} not available")

    # Convert to base first
    if from_cur == BASE:
        amount_in_base = amount
    else:
        # rates[from_cur] = units_of_from_cur per BASE
        # so 1 unit of from_cur = (1 / rates[from_cur]) BASE
        amount_in_base = amount / RATES[from_cur]

    # Convert base to target
    if to_cur == BASE:
        converted = amount_in_base
    else:
        converted = amount_in_base * RATES[to_cur]

    return converted


# --- UI callbacks ---
def on_rates_loaded(base, rates, error=None):
    if error:
        status_label.config(text=f"Failed to load rates: {error}")
        messagebox.showwarning("Rates Error", f"Could not fetch live rates:\n{error}\nUsing limited functionality.")
        return
    status_label.config(text=f"Rates loaded (base: {base})")
    # enable convert button
    convert_btn.config(state=tk.NORMAL)
    refresh_btn.config(state=tk.NORMAL)


def do_refresh_rates():
    status_label.config(text="Refreshing rates...")
    convert_btn.config(state=tk.DISABLED)
    refresh_btn.config(state=tk.DISABLED)
    load_rates_background(on_done=on_rates_loaded)


def convert_currency():
    if not RATES_LOADED:
        messagebox.showerror("No rates", "Exchange rates are not loaded yet. Try Refresh.")
        return
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showwarning("Input Error", "Enter a valid numeric amount.")
        return

    from_cur = from_currency.get().strip().upper()
    to_cur = to_currency.get().strip().upper()

    if from_cur == "" or to_cur == "":
        messagebox.showwarning("Select Currency", "Please select both currencies.")
        return

    try:
        result = convert_amount(amount, from_cur, to_cur)
        result_label.config(text=f"{amount:.2f} {from_cur} = {result:.2f} {to_cur}")
    except KeyError as ke:
        messagebox.showerror("Rate Missing", str(ke))
    except Exception as e:
        messagebox.showerror("Conversion Error", str(e))


# --- Build UI ---
root = tk.Tk()
root.title("Currency Converter (Live)")
root.geometry("420x300")

frame = ttk.Frame(root, padding=12)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Amount:").grid(row=0, column=0, sticky="w")
amount_entry = ttk.Entry(frame)
amount_entry.grid(row=0, column=1, sticky="ew", padx=6)
amount_entry.insert(0, "100")

ttk.Label(frame, text="From:").grid(row=1, column=0, sticky="w")
from_currency = ttk.Combobox(frame, values=["INR","USD","EUR","GBP","JPY"], state="readonly")
from_currency.set("INR")
from_currency.grid(row=1, column=1, sticky="ew", padx=6)

ttk.Label(frame, text="To:").grid(row=2, column=0, sticky="w")
to_currency = ttk.Combobox(frame, values=["INR","USD","EUR","GBP","JPY"], state="readonly")
to_currency.set("USD")
to_currency.grid(row=2, column=1, sticky="ew", padx=6)

convert_btn = ttk.Button(frame, text="Convert", command=convert_currency, state=tk.DISABLED)
convert_btn.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="", font=("Segoe UI", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=2)

status_label = ttk.Label(frame, text="Loading exchange rates...", foreground="blue")
status_label.grid(row=5, column=0, columnspan=2, pady=(12,0))

refresh_btn = ttk.Button(frame, text="Refresh Rates", command=do_refresh_rates, state=tk.DISABLED)
refresh_btn.grid(row=6, column=0, columnspan=2, pady=6)

# Make columns expand
frame.columnconfigure(1, weight=1)

# Start loading rates in background
load_rates_background(on_done=on_rates_loaded)

root.mainloop()
