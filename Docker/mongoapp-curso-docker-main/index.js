import express from 'express'
// Dependencia para conectarse con mongo
import mongoose from 'mongoose'

// Creamos el modelo Animal
const Animal = mongoose.model('Animal', new mongoose.Schema({
  tipo: String,
  estado: String,
}))

// Iniciar la aplicacion
const app = express()

// Conexion de servidor mongoose de docker
                      // user:password@maquinaconexion:puerto/basedatos?confpermisos
mongoose.connect('mongodb://nico:password@monguito:27017/miapp?authSource=admin')

// Endpoints
app.get('/', async (_req, res) => {
  // Busca los animales y los muestra
  console.log('listando... chanchitos...')
  const animales = await Animal.find();
  return res.send(animales)
})
app.get('/crear', async (_req, res) => {
  // Crea un modelo
  console.log('creando...')
  await Animal.create({ tipo: 'Chanchito', estado: 'Feliz' })
  return res.send('ok')
})


app.listen(3000, () => console.log('listening...'))
