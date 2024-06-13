from samplenaming.core.snglobal import CSV_HEADERS, CSV_HEADERS_SHORT
print(CSV_HEADERS)
print(CSV_HEADERS_SHORT)

from samplenaming.core.snsummary import SNSummary

thissummary = SNSummary()
SNSummary.display_entries(thissummary.df, display_style="compact")
thissummary.add_an_entry()
SNSummary.display_entries(thissummary.df, display_style="Full")

elements = ["H"]
style = "INCLUDE" #option: "EXCLUDE"
ids = thissummary.query_by_elements(elements, style=style, reset_df=False)
print("===")

key = "Elements"
thisvalue = "HO"
ids = thissummary.query_by(key, thisvalue)
print("===")

display_cols = ["Composition", "Synthesize", "Syn_params", "QRcode"]
thissummary.query_display(display_style=display_cols)
print("===")

filename = "tmp.csv"
thissummary.query_save(filename="SNquery_results.csv")
