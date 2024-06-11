
# # import click
# from models import db, User, Character, Planet, Vehicle

# """
# In this file, you can add as many commands as you want using the @app.cli.command decorator
# Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
# with youy database, for example: Import the price of bitcoin every night as 12am
# """
# def setup_commands(app):
    
#     """ 
#     This is an example command "insert-test-users" that you can run from the command line
#     by typing: $ flask insert-test-users 5
#     Note: 5 is the number of users to add
#     """
#     # @app.cli.command("insert-test-users") # name of our command
#     # @click.argument("count") # argument of out command
#     # def insert_test_users(count):
#     #     print("Creating test users")
#     #     for x in range(1, int(count) + 1):
#     #         vendedor = Vendedor()
#     #         vendedor.email = "email"
#     #         vendedor.password = "123456"
#     #         vendedor.is_active = True
#     #         db.session.add(vendedor)
#     #         db.session.commit()
#     #         print("User: ", vendedor.email, " created.")

#     #     print("All test users created")

#     # @app.cli.command("insert-test-users") # name of our command
#     # @click.argument("count") # argument of out command
#     # def insert_test_users(count):
#     #         print("Creating test users")
#     #         for x in range(1, int(count) + 1):
#     #             user = User()
#     #             user.email = "test_user" + str(x) + "@test.com"
#     #             user.password = "123456"
#     #             user.is_active = True
#     #             db.session.add(user)
#     #             db.session.commit()
#     #             print("User: ", user.email, " created.")

#     #         print("All test users created")

#     @app.cli.command("fill-db-with-example-data")
#     def fill_db_with_example_data():
#         """ Este comando rellenará la base de datos con datos de ejemplo. """
#         db.drop_all()
#         db.create_all()
#         try:
#             users = [
#                 User(email="davidpadilla@gmail.com", password="123", )


#             ]
#             db.session.add_all(users)
#             db.session.commit()

#             characters = [
#                 Character(id = "1", name = "Luke Skywalker", height = "172", url = "https://www.swapi.tech/api/people/1", description = "A person within the Star Wars universe", eye_color = "blue", hair_color = "blond", skin_color = "fair"),
#                 Character(id = "2", name = "C-3PO", height = "167", url = "https://www.swapi.tech/api/people/2", description = "A person within the Star Wars universe", eye_color = "yellow", hair_color = "n/a", skin_color = "gold"),
#                 Character(id = "3", name = "R2-D2", height = "96", url = "https://www.swapi.tech/api/people/3", description = "A person within the Star Wars universe", eye_color = "red", hair_color = "n/a", skin_color = "white, blue"),
#                 Character(id = "4", name = "Darth Vader", height = "202", url = "https://www.swapi.tech/api/people/4", description = "A person within the Star Wars universe", eye_color = "yellow", hair_color = "none", skin_color = "white"),
#                 Character(id = "5", name = "Leia Organa", height = "150", url = "https://www.swapi.tech/api/people/5", description = "A person within the Star Wars universe", eye_color = "brown", hair_color = "brown", skin_color = "light"),
#                 Character(id = "6", name = "Owen Lars", height = "178", url = "https://www.swapi.tech/api/people/6", description = "A person within the Star Wars universe", eye_color = "blue", hair_color = "brown, grey", skin_color = "light"),
#                 Character(id = "7", name = "Beru Whitesun lars", height = "165", url = "https://www.swapi.tech/api/people/7", description = "A person within the Star Wars universe", eye_color = "blue", hair_color = "brown", skin_color = "light"),    
#                 Character(id = "8", name = "R5-D4", height = "97", url = "https://www.swapi.tech/api/people/8", description = "A person within the Star Wars universe", eye_color = "red", hair_color = "n/a", skin_color = "white, red"), 
#                 Character(id = "9", name = "Biggs Darklighter", height = "183", url = "https://www.swapi.tech/api/people/9", description = "A person within the Star Wars universe", eye_color = "brown", hair_color = "black", skin_color = "light"), 
#                 Character(id = "10", name = "Obi-Wan Kenobi", height = "182", url = "https://www.swapi.tech/api/people/10", description = "A person within the Star Wars universe", eye_color = "blue-gray", hair_color = "auburn, white", skin_color = "fair")                                                          
#             ]
#             db.session.add_all(characters)
#             db.session.commit()

#             planets = [
#                 Planet(uid="1", name="Tatooine", climate="arid", diameter="10465", gravity="1 standard", orbital_period="304", population="200000", rotational_period="23", surface_water="1", terrain="desert"),
#                 Planet(uid="2", name="Alderaan", climate="temperate", diameter="12500", gravity="1 standard", orbital_period="364", population="2000000000", rotational_period="24", surface_water="40", terrain="grassland, mountains"),
#                 Planet(uid="3", name="Yavin IV", climate="temperate, tropical", diameter="10200", gravity="1 standard", orbital_period="4818", population="1000", rotational_period="24", surface_water="8", terrain="jungle, rainforests"),
#                 Planet(uid="4", name="Hoth", climate="frozen", diameter="7200", gravity="1.1 standard", orbital_period="549", population="unknown", rotational_period="23", surface_water="100", terrain="tundra, ice caves, mountain ranges"),
#                 Planet(uid="5", name="Dagobah", climate="murky", diameter="8900", gravity="N/A", orbital_period="341", population="unknown", rotational_period="23", surface_water="8", terrain="swamp, jungles"),
#                 Planet(uid="6", name="Bespin", climate="temperate", diameter="118000", gravity="1.5 (surface), 1 standard (Cloud City)", orbital_period="5110", population="6000000", rotational_period="12", surface_water="0", terrain="gas giant"),
#                 Planet(uid="7", name="Endor", climate="temperate", diameter="4900", gravity="0.85 standard", orbital_period="402", population="30000000", rotational_period="18", surface_water="8", terrain="forests, mountains, lakes"),
#                 Planet(uid="8", name="Naboo", climate="temperate", diameter="12120", gravity="1 standard", orbital_period="312", population="4500000000", rotational_period="26", surface_water="12", terrain="grassy hills, swamps, forests, mountains"),
#                 Planet(uid="9", name="Coruscant", climate="temperate", diameter="12240", gravity="1 standard", orbital_period="368", population="1000000000000", rotational_period="24", surface_water="unknown", terrain="cityscape, mountains"),
#                 Planet(uid="10", name="Kamino", climate="temperate", diameter="19720", gravity="1 standard", orbital_period="462", population="1000000000", rotational_period="27", surface_water="100", terrain="ocean")
#             ]
#             db.session.add_all(planets)
#             db.session.commit()

#             vehicles = [
#                 Vehicle(uid="4", name="Sand Crawler", cargo_capacity="50000", consumables="2 months", cost_in_credits="150000", crew="46", length="36.8", manufacturer="Corellia Mining Corporation", max_speed="30", model="Digger Crawler", passenger="30", vehicle_class="wheeled"),
#                 Vehicle(uid="7", name="X-34 landspeeder", cargo_capacity="5", consumables="unknown", cost_in_credits="10550", crew="1", length="3.4", manufacturer="SoroSuub Corporation", max_speed="250", model="X-34 landspeeder", passenger="1", vehicle_class="repulsorcraft"),
#                 Vehicle(uid="6", name="T-16 skyhopper", cargo_capacity="50000", consumables="2 months", cost_in_credits="150000", crew="46", length="36.8", manufacturer="Corellia Mining Corporation", max_speed="30", model="Digger Crawler", passenger="3", vehicle_class="wheeled"),
#                 Vehicle(uid="8", name="TIE/LN starfighter", cargo_capacity="50000", consumables="2 months", cost_in_credits="150000", crew="46", length="36.8", manufacturer="Corellia Mining Corporation", max_speed="30", model="Digger Crawler", passenger="30", vehicle_class="wheeled"),
#                 Vehicle(uid="14", name="Snowspeeder", cargo_capacity="50000", consumables="2 months", cost_in_credits="150000", crew="46", length="36.8", manufacturer="Corellia Mining Corporation", max_speed="30", model="Digger Crawler", passenger="30", vehicle_class="wheeled"),
#                 Vehicle(uid="18", name="AT-AT", cargo_capacity="50000", consumables="2 months", cost_in_credits="150000", crew="46", length="36.8", manufacturer="Corellia Mining Corporation", max_speed="30", model="Digger Crawler", passenger="30", vehicle_class="wheeled"),
#                 Vehicle(uid="16", name="TIE bomber", cargo_capacity="50000", consumables="2 months", cost_in_credits="150000", crew="46", length="36.8", manufacturer="Corellia Mining Corporation", max_speed="30", model="Digger Crawler", passenger="30", vehicle_class="wheeled"),
#                 Vehicle(uid="19", name="AT-ST", cargo_capacity="50000", consumables="2 months", cost_in_credits="150000", crew="46", length="36.8", manufacturer="Corellia Mining Corporation", max_speed="30", model="Digger Crawler", passenger="30", vehicle_class="wheeled"),
#                 Vehicle(uid="20", name="Storm IV Twin-Pod cloud car", cargo_capacity="50000", consumables="2 months", cost_in_credits="150000", crew="46", length="36.8", manufacturer="Corellia Mining Corporation", max_speed="30", model="Digger Crawler", passenger="30", vehicle_class="wheeled"),
#                 Vehicle(uid="24", name="Sail barge", cargo_capacity="50000", consumables="2 months", cost_in_credits="150000", crew="46", length="36.8", manufacturer="Corellia Mining Corporation", max_speed="30", model="Digger Crawler", passenger="30", vehicle_class="wheeled")


#             ]
#             db.session.add_all(vehicles)
#             db.session.commit()

# #             hobbies = [
# #                 Hobbie(name="Fotografía"),
# #                 Hobbie(name="Ciclismo"),
# #                 Hobbie(name="Dibujo"),
# #                 Hobbie(name="Programación")
# #             ]
# #             db.session.add_all(hobbies)
# #             db.session.commit()
# #             psychologists = [
# #                 Phycologyst(name="Ana", surnames="Pérez", email="
# # ana@mymood.com
# # ", password="secure", experience=5),
# #                 Phycologyst(name="Carlos", surnames="Gómez", email="
# # carlos@mymood.com
# # ", password="secure", experience=7)
# #             ]
# #             db.session.add_all(psychologists)
# #             db.session.commit()
# #             resource_types = [
# #                 ResourceType(resource_type="Artículo"),
# #                 ResourceType(resource_type="Vídeo"),
# #                 ResourceType(resource_type="Imagen"),
# #                 ResourceType(resource_type="Podcast")
# #             ]
# #             db.session.add_all(resource_types)
# #             db.session.commit()
# #             resources = [
# #                 Resource(resource_type_id=resource_types[0].id, url="
# # https://example.com/articulo1
# # ", description="Cómo manejar el estrés", phycologyst_id=psychologists[0].id),
# #                 Resource(resource_type_id=resource_types[1].id, url="https://example.com/video1", description="Meditación para principiantes", phycologyst_id=psychologists[1].id)
# #             ]
# #             db.session.add_all(resources)
# #             db.session.commit()
# #             locations = [
# #                 Location(latitude=40.7128, longitude=-74.0060),
# #                 Location(latitude=34.0522, longitude=-118.2437),
# #                 Location(latitude=41.8781, longitude=-87.6298)
# #             ]
# #             db.session.add_all(locations)
# #             db.session.commit()
# #             # Acciones relacionadas con las categorías de estados de ánimo
# #             actions = [
# #                 Action(action="Hablar con un amigo", description="Compartir tus sentimientos puede ayudar a ver las cosas desde otra perspectiva.", category_id=categories[0].id),  # Feliz/Contento
# #                 Action(action="Escribir en un diario", description="Escribir tus pensamientos puede ayudarte a comprenderlos mejor.", category_id=categories[1].id),  # Triste/Deprimido
# #                 Action(action="Meditación", description="La meditación puede ayudarte a calmar tu mente.", category_id=categories[2].id),  # Ansioso/Estresado
# #                 Action(action="Ejercicio físico", description="El ejercicio puede ayudar a liberar la tensión acumulada.", category_id=categories[3].id)  # Enojado/Frustrado
# #             ]
# #             db.session.add_all(actions)
# #             db.session.commit()
# #             # Historial de estados de ánimo de los usuarios
# #             user_mood_history_entries = [
# #                 UserMoodHistory(user_id=users[0].id, date=datetime.date.today() - datetime.timedelta(days=1), mood_id=moods[0].id),
# #                 UserMoodHistory(user_id=users[1].id, date=datetime.date.today() - datetime.timedelta(days=2), mood_id=moods[1].id),
# #                 UserMoodHistory(user_id=users[2].id, date=datetime.date.today() - datetime.timedelta(days=3), mood_id=moods[2].id)
# #             ]
# #             db.session.add_all(user_mood_history_entries)
# #             db.session.commit()
# #             # Chats entre usuarios
# #             chats = [
# #                 Chat(user_sender_id=users[0].id, user_reciver_id=users[1].id, message_text="¡Hola! ¿Cómo te sientes hoy?", time=datetime.datetime.now() - datetime.timedelta(hours=1)),
# #                 Chat(user_sender_id=users[1].id, user_reciver_id=users[0].id, message_text="Hola, me siento bastante bien, ¿y tú?", time=datetime.datetime.now() - datetime.timedelta(minutes=50)),
# #                 Chat(user_sender_id=users[0].id, user_reciver_id=users[1].id, message_text="También estoy bien, gracias por preguntar.", time=datetime.datetime.now() - datetime.timedelta(minutes=30)),
# #             ]
# #             db.session.add_all(chats)
# #             db.session.commit()
#             print("La base de datos ha sido poblada con datos de ejemplo.")
#         except Exception as e:
#             db.session.rollback()
#             print(f"Error al llenar la base de datos: {e}")









#     @app.cli.command("insert-test-data")
#     def insert_test_data():
#         pass