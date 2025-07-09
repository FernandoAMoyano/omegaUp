from typing import List

#---------------------------------------------------------------

def main():
    amount_of_toys = int(input("Ingresa la cantidad de juguetes"))
    levels_of_fun: List[int] = []


    for i in range(1, amount_of_toys + 1):
        level_of_fun = int(
            input(f"Ingresa el nivel de diversion para el juguete {i}")
        )
        levels_of_fun.append(level_of_fun)
        
    resultado=calculate_the_fun_level(levels_of_fun)
    print(f"quitando el juguete con menor puntaje, el puntaje total es: {resultado}")

#---------------------------------------------------------------

def calculate_the_fun_level( levels_of_fun: list[int] ):
    total_fun=sum(levels_of_fun)
    lower_score=min(levels_of_fun)
    return total_fun - lower_score

#---------------------------------------------------------------

if __name__ == "__main__":
    main()

