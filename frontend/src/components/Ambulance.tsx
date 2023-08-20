import { useState,useEffect } from "react"
import ambulance from "../assets/lottie/ambulance.json"
import Lottie from "lottie-react"
import axios from "axios";

export default function Ambulance(){
    const [ambulances, setAmbulances] = useState(false)
    const [latitude,setLatitude] = useState(0)
    const [longitude,setLongitude] = useState(0)

    useEffect(()=>{
        navigator.geolocation.getCurrentPosition(function(position) {
            setLatitude(position.coords.latitude)
            setLongitude(position.coords.longitude) 
        })
        axios({
            method: 'post',
            url: 'http://localhost:3010/',
            data: {
              lat: latitude,
              long: longitude
          }
          });
    },[latitude,longitude])
    return(
        <div className="flex flex-col items-center text-white bg-cover">
            <h1 className="text-6xl mb-8 tracking-wide font-bold">
                Emergency Vehicle Alert System
            </h1>
            {!ambulances &&
                <div className="w-5/12 flex flex-col items-center" onClick={() => setAmbulances((ambulances)=>!ambulances)}>
                    <Lottie animationData={ambulance} className="w-full h-full mb-40"/>
                    <button className="bg-white text-black p-4 text-2xl font-semibold border rounded-lg">
                        Alert Police
                    </button>
                </div>
            }
            {ambulances &&
                <div>
                    <h1 className="text-center text-2xl mb-12">
                        Police have been alerted, they are currently clearing the fastest corridor 🚨
                    </h1>
                    <iframe src="./final.html" width={1366} height={768}></iframe>
                </div>
            }
        </div>
    )
}