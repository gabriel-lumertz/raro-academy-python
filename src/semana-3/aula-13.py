class Student:
    school_name = 'RaroLabs' # Variável de Classe
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, new_age):
        self.age = new_age

    # Parâmetro CLS faz referência para classe
    @classmethod
    def change_school(cls, name):
        Student.school_name = name
        print(Student.school_name) # Acessando a variável de classe

    # Método Estático
    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'Migração de dados':
            requirement = ['tarefa_1', 'tarefa_2', 'tarefa_3']
        else:
            requirement = ['tarefa_1']
        return requirement
            
objeto_alberto = Student('Alberto Silva', 17)
objeto_bia = Student('Bia Marins', 27)

print(f'Nome: {objeto_alberto.name}\t Idade: {objeto_alberto.age}\t {Student.school_name}')
print(f'Nome: {objeto_bia.name}\t Idade: {objeto_bia.age}\t {Student.school_name}')

print(Student.gather_requirement('Carga de dados'))
print(objeto_bia.gather_requirement('Tela Login autenticada'))
print(objeto_alberto.gather_requirement('Migração de dados'))

objeto_alberto.set_age(34)
Student.change_school('Raro Academy - Python')

print(f'Nome: {objeto_alberto.name}\t Idade: {objeto_alberto.age}\t {objeto_alberto.school_name}')
print(f'Nome: {objeto_bia.name}\t Idade: {objeto_bia.age}\t {objeto_bia.school_name}')


# Student.change_school('Raro Academy - Python') # Chamada método de classe