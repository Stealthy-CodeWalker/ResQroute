const express = require("express")
const app = express()
const cors = require('cors');

app.use(cors({
    origin: '*',
    credentials: true,
}));

const port = 3010
const {spawn} = require("child_process")

app.use(express.json())

app.get("/",function(req,res){
    console.log(req)
    const { lat, long } = req.body
    console.log(lat, long)
    const process = spawn('python', ["./test.py", lat,long]);
    process.stdout.on('data', (data)=>{
        console.log(`${data}`)
    })
    res.send('aee.html');
}
);


app.listen(port);