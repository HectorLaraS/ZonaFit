from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from abc import ABC, abstractmethod
from typing import Optional
from src.utils.password import *
from src.Domain.client import *
from src.Domain.person import *
from src.Domain.user import *
from src.Storage.DB import *
from src.Storage.user_persistence import *
from src.Storage.client_persistence import *
from src.Storage.person_persistence import *
from src.Storage.user_mysql import *
from src.Storage.client_mysql import *
from src.Storage.person_mysql import *
from src.Service.user_service import *
from src.Service.client_service import *
from src.Service.person_service import *
from src.utils.HelpFunctions import *

class ClientController:
    def __init__(self):
        pass

    def cargar_datos(self):
        service_client = bootstrap_service_client()
        service_person = bootstrap_service_person()
        lst_clientes: list[Client] = service_client.get_all()
        lst_persons: list[Person] = service_person.get_all()
        lst_output = []
        for client in lst_clientes:
            for person in lst_persons:
                if person.id == client.person_id:
                    client.fullname = f"{person.name} {person.last}"
                    client.email = person.email
                    client.phone = person.phone
                    lst_output.append((client.person_id,client.fullname, client.membership_type,client.id
                                           , client.next_payment.strftime("%d/%m/%Y"), bool(client.payment_pending)
                                       ,client.email, client.phone))
        return lst_output

    def agregar_usuario(self, elements):
        service_client = bootstrap_service_client()
        service_person = bootstrap_service_person()
        persona = Person(
            name=str(elements[0]),
            last=str(elements[1]),
            email=str(elements[3]),
            phone=str(elements[4])
        )
        print(service_person.add(persona))
        new_person: Person = service_person.get_by_email(persona.email)
        persona.id = new_person.id
        cliente = Client(
            person_id=persona.id,
            membership_type=elements[2],
            payment_pending=False
        )
        service_client.add(cliente)
        ##print(cliente, cliente.last_payment,cliente.next_payment)

    def editar_usuario(self, elements):
        service_client = bootstrap_service_client()
        service_person = bootstrap_service_person()
        persona = Person(
            name=str(elements[0]),
            last=str(elements[1]),
            email=str(elements[3]),
            phone=str(elements[4])
        )

        new_person: Person = service_person.get_by_email(persona.email)
        persona.id = new_person.id
        print(persona)
        persona.id = new_person.id
        print(service_person.update(persona))
        new_date = datetime.strptime(elements[5], "%d/%m/%Y")
        new_next_payment = new_date + relativedelta(months=1)
        cliente = Client(
            person_id=persona.id,
            membership_type=elements[2],
            payment_pending=False,
            last_payment=new_date,
            next_payment=new_next_payment
        )
        new_client: Client = service_client.get_by_user_id(cliente.person_id)
        cliente.id = new_client.id
        print("LO QUE SIGUE ES EL METODO UPDATE")
        print(service_client.update(cliente))

    def eliminar_usuario(self, elements: list):
        service_client = bootstrap_service_client()
        service_person = bootstrap_service_person()
        persona = Person(
            name=str(elements[0]),
            last=str(elements[1]),
            email=str(elements[3]),
            phone=str(elements[4])
        )
        print("*** PERSONA ***")
        new_person: Person = service_person.get_by_email(persona.email)
        persona.id = new_person.id
        print(service_person.remove(persona))
        cliente = Client(
            person_id=persona.id,
            membership_type=elements[2],
            payment_pending=False
        )
        print(cliente)



if __name__ == "__main__":
    cliente_controller = ClientController()
    tmp_lst = cliente_controller.cargar_datos()
    for client in tmp_lst:
        print(client)