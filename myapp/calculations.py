def Calculations(Loan,Markup,Period,Processing):
    try:
        Monthly_Markup = float(Markup)/12
        Total_periods_markup = float(Monthly_Markup * Period) 
        Markup_Amount = ((Total_periods_markup/100)*Loan)
        Total_Amount = (Markup_Amount + Loan)
        Installment = (Total_Amount/Period)
        if Installment % 10 != 0:
            remainder = Installment % 10
            Installment = Installment - remainder
            Installment += 10
        else:
            pass
        Processing_Fee = ((Processing/100)*Loan)
        return [int(Total_Amount),int(Markup_Amount),int(Installment),int(Processing_Fee)]
    except:
        print('Except block is working here')



