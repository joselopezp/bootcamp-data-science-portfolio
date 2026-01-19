"""Menu which is neccesary for enter data and User Experiencie (UX)."""

from contact import Contact, ContactManager


def main():
    manager = ContactManager()
    
    while True: 
        print("\n" + "="*40)
        print("   SISTEMA DE GESTION DE CONTACTOS")
        print("="*40)
        print("1. Agregar contacto")
        print("2. Buscar por nombre")
        print("3. Buscar por teléfono")
        print("4. Editar contacto")
        print("5. Eliminar contacto por número")
        print("6. Ver todos los contactos")
        print("7. Exportar contactos a CSV")
        print("0. Salir")
        print("="*40)
        
        option = input("Seleccione una opción: ")
        
        match option:
            case "1":
                add_contact(manager)
            case "2":
                search_by_name(manager)
            case "3":
                search_by_phone(manager)
            case "4":
                edit_contact(manager)
            case "5":
                delete_contact_by_number(manager)
            case "6":
                show_all(manager)
            case "7":
                export_contacts(manager)
            case "0":
                print("Hasta luego")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
                
                
def add_contact(manager):
    print("\n--- Agregar contacto ---")
    
    while True:
        name = input("Nombre: ")
        phone = input("Teléfono: ")
        email = input("Correo electrónico: ")
        address = input("Dirección: ")
        
        try: 
            contact = Contact(name, phone, email, address)
            if manager.add(contact):
                print("✓ Contacto agregado exitosamente")
            else:
                print("✗ Ya existe un contacto con ese nombre")
            break
        except ValueError as e:
            print(f"✗ Error: {e}")
            while True:
                retry = input("¿Desea intentar de nuevo? (s/n): ").lower().strip()
                if retry in ["s", "n"]:
                    break
                print("Por favor ingrese 's' para sí o 'n' para no.")
            if retry != "s":
                break
        
def show_all(manager):
    """Displays all contacts with aligned row indices for readability."""
    print("\n--- Todos los Contactos ---")
    contacts = manager.get_all()

    if contacts:
        # Determine the width needed to align indices based on total count
        width = len(str(len(contacts)))

        for index, contact in enumerate(contacts, start=1):
            # Right-align the index so multi-digit numbers line up vertically
            aligned_index = str(index).rjust(width)
            print(f"[{aligned_index}] {contact}")
            print("-" * 40)
    else:
        print("No hay contactos registrados.")
        
def search_by_name(manager):
    print("\n--- Buscar por Nombre---")
    name = input("Nombre a buscar: ")
    results = manager.search_by_name(name)
    
    if results:
        print(f"Se encontraron {len(results)} contacto(s):")
        for contact in results:
            print(f"   {contact}")
    else:
        print("No se encontraron contactos.")
        
     
def search_by_phone(manager):
    print("\n--- Buscar por Teléfono ---")
    phone = input("Teléfono a buscar: ")
    results = manager.search_by_phone(phone)
    
    if results:
        print(f"Se encontraron {len(results)} contacto(s):")
        for contact in results:
            print(f"  {contact}")
    else:
        print("No se encontraron contactos.")
        
def edit_contact(manager):
    """Edit an existing contact's information."""
    print("\n--- Editar Contacto ---")
    name = input("Nombre del contacto a editar: ")
    
    # Verify contact exists
    results = manager.search_by_name(name)
    if not results:
        print("No se encontró el contacto.")
        return
    
    print(f"Contacto encontrado: {results[0]}")
    print("\nDeje en blanco los campos que no desea modificar:")
    
    new_name = input("Nuevo nombre: ").strip()
    new_phone = input("Nuevo teléfono: ").strip()
    new_email = input("Nuevo correo: ").strip()
    new_address = input("Nueva dirección: ").strip()
    
    # Build dictionary only with non-empty fields
    new_data = {}
    if new_name:
        new_data["name"] = new_name
    if new_phone:
        new_data["phone"] = new_phone
    if new_email:
        new_data["email"] = new_email
    if new_address:
        new_data["address"] = new_address
    
    if not new_data:
        print("No se realizaron cambios.")
        return
    
    try:
        if manager.edit(name, **new_data):
            print("✓ Contacto editado exitosamente")
        else:
            print("✗ No se encontró el contacto")
    except ValueError as e:
        print(f"✗ Error: {e}")

def delete_contact_by_number(manager):
    """Delete a contact using its displayed number."""
    print("\n--- Eliminar Contacto por Número ---")
    contacts = manager.get_all()

    if not contacts:
        print("No hay contactos registrados.")
        return

    width = len(str(len(contacts)))
    for index, contact in enumerate(contacts, start=1):
        aligned_index = str(index).rjust(width)
        print(f"[{aligned_index}] {contact}")
        print("-" * 40)

    try:
        number = int(input("Ingrese el número del contacto a eliminar: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    if not (1 <= number <= len(contacts)):
        print("Número fuera de rango.")
        return

    contact_to_delete = contacts[number - 1]

    print(f"\nContacto seleccionado:\n{contact_to_delete}")

    while True:
        confirm = input("\n¿Está seguro que desea eliminar este contacto? (s/n): ").lower().strip()
        if confirm in ("s", "n"):
            break
        print("Por favor ingrese 's' para sí o 'n' para no.")

    if confirm == "s":
        if manager.delete_contact(contact_to_delete):
            print("✓ Contacto eliminado exitosamente")
        else:
            print("✗ Error al eliminar el contacto")
    else:
        print("Operación cancelada.")
        
def export_contacts(manager):
     """Export contacts to a CSV file."""
     print("\n--- Exportar Contactos a CSV ---")
     file_name = input("Nombre del archivo (ej: contactos.csv): ").strip()
 
     if not file_name:
         print("Nombre de archivo no válido.")
         return
 
     if not file_name.lower().endswith(".csv"):
         file_name += ".csv"
 
     try:
         manager.export_to_csv(file_name)
         print(f"✓ Contactos exportados exitosamente a '{file_name}'")
     except OSError as error:
         print(f"✗ Error al crear el archivo: {error}")



        
if __name__ == "__main__":
    main()   
            
            
        
        