import requests
import tkinter as tk

def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        pokemon_name = data["name"].capitalize()
        pokemon_id = data['id']
        height = data['height'] / 10   
        weight = data['weight'] / 10   

        stats_text = ""
        for stat in data['stats']:
            stat_name = stat["stat"]["name"]
            stat_value = stat["base_stat"]
            stats_text += f"{stat_name}: {stat_value}\n"

        return f"Pokemon: {pokemon_name} (ID: {pokemon_id})\nHeight: {height} m\nWeight: {weight} kg\n\nStats:\n{stats_text}"
    else:
        return "No pokemon found."

def open_new_screen(nick,result):
    new_screen= tk.Toplevel(screen)
    new_screen.title(f"Pokemon {nick}")
    new_screen.geometry("300x400")

    infoLabel = tk.Label(new_screen,text=result,font=('Arial',16,"bold"))
    infoLabel.pack(pady=20)

def click_button():
    nick = entryUser.get()
    result = get_pokemon(nick)
    if get_pokemon(nick) == "No pokemon found.":
        resultLabel.config(text="unsuccessful",fg="red")
        
    else:
        resultLabel.config(text="Succes",fg="green")
        open_new_screen(nick,result)
        
#window
screen = tk.Tk()
screen.title("Pokemon App")
screen.minsize(height=600,width=800)
screen.configure(bg="lightblue")

#label
pokemon = tk.Label(
    text="Enter Pokemon:",
    font=('Arial', 15, "normal"),
    bg="lightblue",
    fg="darkblue"
)
pokemon.place(x=200, y=250)


#entry
entryUser = tk.Entry(width=20)
entryUser.place(x=350,y=257)

#button
buttonUser = tk.Button(text="Ok",width=5,height=1,command=click_button,bg="lightblue",fg="white").place(x=500,y=253)

#resultLabel
resultLabel = tk.Label(text="",font=('Arial',12,"bold"),bg="lightblue")
resultLabel.place(x=300,y=500)

screen.mainloop()
