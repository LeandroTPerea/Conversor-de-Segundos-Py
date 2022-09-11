segundos_str = input("Por favor,entre com o número em segundos que deseja converter:")

total_segs = int(segundos_str)

dias = total_segs //(24*60*60)

horas = total_segs //(60*60)%24 
              
segs_restantes = total_segs %(60*60)

minutos = segs_restantes//60


segs_restantes_final = segs_restantes % 60

print(dias,"dias,",horas,"horas,",minutos, "minutos e",segs_restantes_final,"segundos.")
