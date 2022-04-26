import threading

from pyswip import Prolog
from time import gmtime, strftime, time
import make_prolog_file


def invoke_prolog(Data_class, rest):
    start_time = time()
    #print(threading.get_native_id())

    result_file_name = "automation_results/" + strftime("%Y_%m_%d_%H_%M_%S", gmtime()) + ".txt"
    print(result_file_name)
    f = open(result_file_name, "w")
    f.close()

    data = Data_class.get_data()
    # Teeb saadud HA seadmete/teenuste andmete põhjal Prolog faili, kus on lisaks kasutaja poolt tehtud automatsioonid
    with open("prolog_files/automation_final.pl", 'w') as file:

        make_prolog_file.add_facts(data, file)

        # Võtame kõik täiturid minu poolt tehtud predikaatidest, sest meil on seda vaja, et hiljem
        # kontrollida millised automatsiooni reeglis olevatest predikaaditest on täiturid
        #make_prolog_file.add_init_preds(file, result_file_name)

        automation_result_rule = ["write_output(Response):-\n", "%<insert_result_name>", "\twrite(Out, Response),\n",
                                  "\tclose(Out).\n"]

        for line in automation_result_rule:
            if line == "%<insert_result_name>":
                file.write("\topen('" + result_file_name + "', append, Out),\n")
            else:
                file.write(line)
        file.write('\n')

        # Kirjutame kõik kasutaja poolt tehtud reeglid Prolog faili ning kogume kokku kõikide reeglite päised, et hiljem
        # saaks nende pihta päringuid teha.
        predicates = make_prolog_file.get_users_rules(data, file)

    prolog = Prolog()
    prolog.consult("prolog_files/automation_final.pl")
    prolog.consult("prolog_files/init_preds.pl")
    #prolog.consult("prolog_files/automation_rules.pl")
    prolog.consult("prolog_files/multiple_rules_exec_test.pl")

    print(predicates)
    for pred in predicates:
        res = list(prolog.query(pred))

    with open(result_file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            rest.send_state(line, data)

    print("--- %s seconds ---" % (time() - start_time))
