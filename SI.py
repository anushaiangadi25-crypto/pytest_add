def calculate_SI(principle,interest,time):
    return(principle*interest*time)/100;
if __name__=="__main__":

    
    p = float(input("Enter Principal: "))
    r = float(input("Enter Rate (%): "))
    t = float(input("Enter Time (years): "))

    print(f"Simple Interest: {(p * r * t) / 100}")