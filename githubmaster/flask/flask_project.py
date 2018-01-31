
# coding: utf-8

# In[2]:

from flask import Flask,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from basededatos import Base, Restaurant,MenuItem
engine=create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
DBsession=sessionmaker(bind=engine)
session=DBsession()
app=Flask(__name__)
@app.route('/')
@app.route('/restaurante/<int:id_restaurante>')
def menu(id_restaurante):
    restaurante=session.query(Restaurant).filter_by(id=id_restaurante)[0]
    items=session.query(MenuItem).filter_by(id=id_restaurante)
    return render_template('menu.html',restaurante=restaurante,items=items)
    return output
@app.route('/restaurante/<int:id_restaurante>/nuevo',methods=['GET','POST'])
def Nuevo_item_menu(id_restaurante):
	if request.method =='POST':
		nuevo_item=MenuItem(name= request.form['nombre'],restaurante_id=id_restaurante)
		session.add(nuevo_item)
		session.commit()
		return redirect(url_for('menu', id_restaurante=id_restaurante))
	else:
		return render_template('nuevo.html', id_restaurante=id_restaurante)

@app.route('/restaurante/<int:id_restaurante>/<int:id_menu>/editar/')	
def Editarmenu(id_restaurante,id_menu):
	return 'Pagina para editar el menu de un restaurante'
@app.route('/restaurante/<int:id_restaurante>/<int:id_menu>/eliminar')
def eliminar_menu(id_restaurante,id_menu):
	return 'Pagina para eliminar del menu'
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=8000)

