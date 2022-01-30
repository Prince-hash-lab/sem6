import pandas as pd
import numpy as np
import logging
import sys

iserror=False
# def check_exception():
n=len(sys.argv)
if n!=2:
    iserror=True
    logging.error('give correct number of parameters>>> one parameter= file_name.csv')
    raise Exception("give correct number of parameter>>>> one parameter= file_name.csv ")
    logging.shutdown()
    # exit()
else:
    fl_name=sys.argv[1]
    tap=np.char.isnumeric(fl_name)
    if tap==True:
        iserror=True
        logging.error("Enter non integer filename")
        raise Exception("Enter non integer filename")
        logging.shutdown()
        # exit()
    else:
        try:
            db=pd.read_csv(fl_name)
            if len(db.columns)!=3:
                iserror=True
                logging.error("Only 3 columns are allowed in input file")
                raise Exception("Only 3 columns are allowed in input file")
                logging.shutdown()
                # exit()
            else:
                col1=db.columns
                col2=['RollNumber', 'Submission', 'Marks']
                for i in range(len(col1)):
                    if col1[i]!=col2[i]:
                        iserror=True
                        logging.error('Columns name should be in "RollNumber" , "Submission", "Marks"')
                        raise Exception('Columns name should be in "RollNumber" , "Submission", "Marks"')
                        logging.shutdown()
                        # exit()
        except IOError:
            iserror=True
            logging.error('File not found')
            print("File not found ")
            # exit()
        logging.shutdown()
        

def unique(list1):
    list_set=set(list1)
    unique_list=list(list_set)
    return unique_list

def main():
    logging.basicConfig(filename='101916056-1.log', level=logging.INFO)
    # check_exception()
    if iserror==False:
        # print("bas khatam 1")
        df = pd.read_csv(sys.argv[1])
        lt=[]
        for i in range(len(df)):
            lt.append(df.iloc[i][0])
        lt=unique(lt)
        lt.sort()
        odf=pd.DataFrame({"RollNumber":lt, 'P1':[0 for i in range(len(lt))], 'P2':[0 for i in range(len(lt))],'P3':[0 for i in range(len(lt))],'P4':[0 for i in range(len(lt))],'P5':[0 for i in range(len(lt))]})
        for j in range(len(df)):
            roll=df.RollNumber[j]
            sub=df.Submission[j]
            mark=df.Marks[j]
        #     if sub=='P4':
        #         print('yes')
        #     print(roll, sub, mark)
            index=-1
            for i in range(len(odf)):
                if odf.loc[i,'RollNumber' ]==roll:
                    index=i
                    break;
            if odf.loc[index, sub]!=0:
                strerr="duplicate  at index ", index, " RollNumber ", roll, " sujbect " ,sub
                logging.info(strerr)
            else :
                if str(mark).isnumeric():  
                    odf.loc[index, sub]=int(mark)
                else:
                    odf.loc[index, sub]=mark
        
        p1data={'X':0, 'nan':0, 'NAN':0,'-':0}
        p2data={'X':0, 'nan':0, 'NAN':0,'-':0}
        p3data={'X':0, 'nan':0, 'NAN':0,'-':0}
        p4data={'X':0, 'nan':0, 'NAN':0,'-':0}
        p5data={'X':0, 'nan':0, 'NAN':0,'-':0}
        for ind1 in range(len(odf)):
            for ind2 in range(5):
                if ind2+1==1:
                    dt2=p1data
                elif ind2+1==2:
                    dt2=p2data
                elif ind2+1==3:
                    dt2=p3data
                elif ind2+1==4:
                    dt2=p4data
                elif ind2+1==5:
                    dt2=p5data
                
                mark1=odf.iloc[ind1, ind2+1]
                if str(mark1).isnumeric()==False:
        #         print(mark)
                    odf.iloc[ind1, ind2+1]=0     
                    if mark1!='X' and mark1!='NAN' and mark1!='-':
                        mark1='nan'
                    if mark1=='X':
                        dt2['X']+=1
                    elif mark1=='nan':
                        dt2['nan']+=1
                    elif mark1=='NAN':
                        dt2['NAN']+=1
                    elif mark1=='-':
                        dt2['-']+=1
                    
        strerr="for P1 X : ", p1data['X'], " nan : ", p1data['nan'], " NAN : ", p1data['NAN'],  " - : ", p1data['-']
        logging.info(strerr)
        strerr="for P2 X : ", p2data['X'], " nan : ", p2data['nan'], " NAN : ", p2data['NAN'],  " - : ", p2data['-']
        logging.info(strerr)
        strerr="for P3 X : ", p3data['X'], " nan : ", p3data['nan'], " NAN : ", p3data['NAN'], " - : ", p3data['-']
        logging.info(strerr)
        strerr="for P4 X : ", p4data['X'], " nan : ", p4data['nan'], " NAN : ", p4data['NAN'], " - : ", p4data['-']
        logging.info(strerr)
        strerr="for P5 X : ", p5data['X'], " nan : ", p5data['nan'], " NAN : ", p5data['NAN'], " - : ", p5data['-']
        logging.info(strerr)
        print(odf.head(20))
        print(odf.tail(20))
        odf.to_csv('101916056-output.csv', index=True)


if __name__ == '__main__':
    main()