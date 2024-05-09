# Days to count
DAYS = 7

# Initialize names list
names   = []

# Initialize drivers list using the space-separated input
drivers = [i for i in input().split()]

try:
    if DAYS in range(1, 8):
        # Check if drivers list is not empty
        if len(drivers) != 0:
            # Initialize kms list adding a list for each driver
            kms = [[] for i in drivers]
            # Iterate throught drivers list and, for each day, insert the kms each driver has done
            for driver in range(len(drivers)):
                print('KMs para el conductor {}:'.format(drivers[driver]))
                for day in range(1, DAYS + 1):
                    kms[driver].append(int(input(' Dia {} -> '.format(day))))

            # Initialize total kms list
            total_kms = []
            
            # Get total kms
            for i in kms:
                total_kms.append(sum(i))

            # Display the results
            print('\nConductor', end='\t' * 3)
            print('TOTAL', end='\t')
            for day in range(1, DAYS + 1):
                print('DIA', day, end='\t')
            
            print()
            print('-' * 100)
            
            for driver in range(len(drivers)):
                print(drivers[driver], end='\t' * 4)
                print(total_kms[driver], end='\t')
                for day in kms[driver]:
                    print(day, end='\t')
                
                print()
        else:
            print('[!] No se ha introducido ningun conductor!')
    else:
        print('[!] Numero de dias de la semana invalido!')
except ValueError:
    print('[!] Los km deben ser enteros!')