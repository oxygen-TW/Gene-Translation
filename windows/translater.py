import os.path
import sys
#胺基酸轉換標準樣本
Base_dict = dict({
#U**
"UUU":"Phe",
"UUC":"Phe",
"UUA":"Leu",
"UUG":"Leu",
"UCU":"Ser",
"UCC":"Ser",
"UCA":"Ser",
"UCG":"Ser",
"UAU":"Tyr",
"UAC":"Tyr",
"UAA":"STOP", #終止密碼子
"UAG":"STOP", #終止密碼子
"UGU":"Cys",
"UGC":"Cys",
"UGA":"STOP", #終止密碼子
"UGG":"Trp",
#C**
"CUU":"Leu",
"CUC":"Leu",
"CUA":"Leu",
"CUG":"Leu",
"CCU":"Pro",
"CCC":"Pro",
"CCA":"Pro",
"CCG":"Pro",
"CAU":"His",
"CAC":"His",
"CAA":"Gln",
"CAG":"Gln",
"CGU":"Arg",
"CGC":"Arg",
"CGA":"Arg",
"CGG":"Arg",
#A**
"AUU":"Ile",
"AUC":"Ile",
"AUA":"Ile",
"AUG":"START", #起始密碼子
"ACU":"Thr",
"ACC":"Thr",
"ACA":"Thr",
"ACG":"Thr",
"AAU":"Asn",
"AAC":"Asn",
"AAA":"Lys",
"AAG":"Lys",
"AGU":"Ser",
"AGC":"Ser",
"AGA":"Arg",
"AGG":"Arg",
#G**
"GUU":"Val",
"GUC":"Val",
"GUA":"Val",
"GUG":"Val",
"GCU":"Ala",
"GCC":"Ala",
"GCA":"Ala",
"GCG":"Ala",
"GAU":"Asp",
"GAC":"Asp",
"GAA":"Glu",
"GAG":"Glu",
"GGU":"Gly",
"GGC":"Gly",
"GGA":"Gly",
"GGG":"Gly"
})

#讀取mRNA序列
def fileRead(file_name):
    if os.path.exists(file_name):
        fileI = open(file_name,'r')
        rna = fileI.read()
        fileI.close()
        
        print("complete -> "+file_name + " 成功載入")
        return rna
    else:
        print("Error 10 -> 找不到.mrna檔案，你是否忘記輸入.mrna副檔名?\n")
        exit(10)

#輸出tRNA序列
def FileOut(file_name,amino,resolve_count):
    try:    
        fileO = open(file_name + ".amino","w")    
        fileO.write(amino)

        print("complete -> "+file_name+".amino"+" 檔案已產生，共寫入 " + str(resolve_count) + " 個胺基酸序")
    except:
        print("Error 11 -> 檔案寫入失敗，請檢查檔案系統")
        
    finally:
        fileO.close()

#解析胺基酸與轉譯行為
def resolve(base3,resolve_count):
    #base3 = base3.upper()
    #print(Base_dict[base3])
    if not(base3 in Base_dict):
        print ("Error 20 -> 無法識別的鹼基對 at "+str(resolve_count)+"\n")
        #print(mrna + base3)
        return "Err"
    elif Base_dict[base3] == "STOP":
        End_base = base3
        return "END"
    else:
        #print(Base_dict[base3])
        return Base_dict[base3]

#檢查鹼基序是否完整以及定位起始密碼子
def check(mrna_split):
    if not("AUG" in mrna_split):
        print("Warning 30 -> 找不到起始密碼子")
        sw = ""
        while sw != "y" and sw != "n":
            sw = input("是否從頭轉譯，除非你很清楚你在做甚麼，否則可能導致轉譯失敗(y/n)")
            if sw == "y":
                start=0
            elif sw == "n":
                print("\nExit")
                return -1
    else:
        start = mrna_split.index("AUG")
        print("complete ->  起始密碼子已定位")
    
    if not("UAA" in mrna_split) and not("UAG" in mrna_split) and not("UGA" in mrna_split):
        print("Warning 31 -> 找不到終止密碼子，mRNA是否不完整? 可能導致轉譯錯誤")

    else:
        print("complete ->  終止密碼子已確定")
    return start
#Program Entry
def main():
    try:
        file_name = sys.argv[1]

    except:
        print("Error 41 -> 參數錯誤或沒有參數")
        exit()
        
    #file_name=input("讀取檔名.mrna ->")
    mrna = str(fileRead(file_name))
    ok = True
    
    #分割為鹼基組
    n = 3
    #print([mrna[i:i+n] for i in range(0, len(mrna), n)])
    mrna_split = [mrna[i:i+n] for i in range(0, len(mrna), n)]
    mrna_split = [x.upper() for x in mrna_split] #To upper
    
    amino = ""
    
    #print ("AUG" in mrna_split)
    start = check(mrna_split)
    ok=False if start==-1 else True
    
    if ok:
        print("Info -> 開始轉譯")
        resolve_count = 0
        
        for i in range(start,len(mrna_split)):
            #print(mrna_split[i])
            resolve_count += 1
            if resolve(mrna_split[i],resolve_count) == "Err":   
                ok = False
                break
                
            elif resolve(mrna_split[i],resolve_count) == "END":
                amino += mrna_split[i]
                print("Info -> 轉譯至終止密碼子")
                break
                
            elif resolve(mrna_split[i],resolve_count) == "START":
                amino += "AUG "
                
            else:
                amino += resolve(mrna_split[i],resolve_count) + " "
        if ok:
            #print (resolve_count)
            print("complete -> 轉譯完成")
            #print(amino)
            
            FileOut(file_name,amino,resolve_count)
        else:
            print("Error ->  轉譯失敗")
            
if __name__ == "__main__":
    main()