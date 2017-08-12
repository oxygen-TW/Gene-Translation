import os
import sys

#鹼基轉換標準樣本
Base_dict = dict({"A":"U","C":"G","G":"C","T":"A"})

#讀取DNA序列
def fileRead(file_name):
    if os.path.exists(file_name):
        fileI = open(file_name ,'r')
        rna = fileI.read()
        fileI.close()
        
        print("complete -> "+file_name + " 成功載入")
        return rna
    else:
        print("Error 10 -> 找不到.dna檔案，你是否忘記輸入.dna副檔名?\n")
        exit(10)
    
#解析鹼基與轉錄行為
def resolve(base,resolve_count):
    base = base.upper()
    if base == " ":
        return ""
    
    if not(base in Base_dict):
        print ("Error 20 -> 位無法識別的鹼基 at "+str(resolve_count)+"\n")
        #print(mrna + base)
        return "E"
    else:
        return Base_dict[base]

#輸出mRNA序列
def FileOut(mrna,file_name):
    try:    
        fileO = open(file_name + ".mrna","w")    
        textnum = fileO.write(mrna)
        print("complete -> 轉錄完成 "+file_name+".mrna"+" 檔案已產生，共寫入 " + str(textnum) + " 個鹼基")
    except:
        print("Error 11 -> 檔案寫入失敗，請檢查檔案系統")
        
    finally:
        fileO.close()

#Program Entry
def main():
    try:
        file_name = sys.argv[1]
    except:
        print("Error 41 -> 參數錯誤或沒有參數")
        exit()
    #file_name=input("讀取檔名.dna ->")    
    rna = fileRead(file_name)
    mrna = ""
    resolve_count = 0
    ok = True
    
    for base in rna:
        resolve_count += 1
        if resolve(base,resolve_count) == "E":   
            ok = False
            break;
        else:
            if resolve(base,resolve_count) != "":
                mrna += resolve(base,resolve_count)
            
    #如果轉錄過程沒有異常，呼叫輸出
    if ok:
        FileOut(mrna,file_name)
    
if __name__ == "__main__":
    main()


