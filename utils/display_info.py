def display_etappe(etappe, bruker_variabler):
    display_message = f"{etappe.time_start}-{etappe.time_end}:"

    for i in range(len(bruker_variabler)):
        if (bruker_variabler[i].lower() == 'temperatur'):
            display_message += f" fra {etappe.low} til {etappe.high} grader (snittemperatur {etappe.temp} grader)"
        if (bruker_variabler[i].lower() == 'regn'):
            display_message += f" {etappe.regn}mm regn"
        if (bruker_variabler[i].lower() == 'vind'):
            display_message += f" {etappe.vind} m/s"
    display_message += "\n"
    # print(f"{etappe.time_start}-{etappe.time_end}: fra {etappe.low} til {etappe.high} grader (snittemperatur {etappe.temp} grader) {etappe.regn}mm regn {etappe.vind} m/s\n")
    print(display_message)

def display_day(dag):
    uke = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]
    month= ["Januar","Februar","Mars","April","Mai","Juni","Juli","August","September","Oktober","November","Desember",
  ]
    display_message = f"\n{uke[dag.ukedag]} {dag.date_isoformat[8: 10]}.{month[int(dag.date_isoformat[5: 7]) - 1]} {dag.date_isoformat[0: 4]} "

    for i in range(len(dag.bruker_variabler)):
        if (dag.bruker_variabler[i].lower() == 'temperatur'):
            display_message += f"(snittemperatur {dag.total_temp / dag.count} grader) "
        if (dag.bruker_variabler[i].lower() == 'regn'):
            display_message += f"{dag.total_regn}mm regn "
        if (dag.bruker_variabler[i].lower() == 'vind'):
            display_message += f"snittvind {dag.total_vind / dag.count} m/s "
    display_message += ":\n"

    print(display_message)
    # print(f"{uke[dag.ukedag]} {dag.date_isoformat[8: 10]}.{month[int(dag.date_isoformat[5: 7]) - 1]} {dag.date_isoformat[0: 4]} (snittemperatur {dag.total_temp / dag.count} grader) : {dag.total_regn}mm regn snittvind {dag.total_vind / dag.count} m/s \n")
    
    for i in range(len(dag.etapper)):
        display_etappe(dag.etapper[i], dag.bruker_variabler)

def display_uke(uke_liste):
    for i in range(len(uke_liste)):
        display_day(uke_liste[i])
