from flet import CupertinoTextField,Ref

# Define a dictionary with proper references to CupertinoTextField elements
dic_fields = {
    'Loan Amount': Ref[CupertinoTextField](),
    'Markup Rate': Ref[CupertinoTextField](),
    'Installment': Ref[CupertinoTextField](),
    'Processing Rate': Ref[CupertinoTextField](),
}
