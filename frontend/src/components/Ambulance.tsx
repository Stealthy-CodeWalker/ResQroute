import { useState,useEffect } from "react"
import waiting from "../assets/lottie/waiting.json"
import Lottie from "lottie-react"
import axios from "axios";

export default function Ambulance(){
    // let latitude=0,longitude=0;
    const [data,setData] = useState("")
    const [ambulances, setAmbulances] = useState(false)
    const [latitude,setLatitude] = useState(0)
    const [longitude,setLongitude] = useState(0)
    // const [loading,setLoading] = useState(false)
    // const Loc =() =>{
    //     navigator.geolocation.getCurrentPosition(function(position) {
    //         latitude = position.coords.latitude
    //         longitude = position.coords.longitude
    //         console.log("Latitude is :", position.coords.latitude);
    //         console.log("Longitude is :", position.coords.longitude);
    //     })
    // }

    // const loc = JSON.stringify({
    //     "lat": latitude,
    //     "long": longitude
    //   });

    // const config = {
    // method: 'get',
    // maxBodyLength: Infinity,
    // url: 'http://localhost:3010/',
    // headers: { 
    //     'Content-Type': 'application/json'
    // },
    // data : loc
    // };

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
    },[ambulances])
    const Open = () =>{
        // Loc()
        window.open('./aee.html')
        return(
            <div>
                    <h1 className="text-2xl">
                        Police received Ambulance Request
                    </h1>
                </div>
        )
    }
    return(
        <div className="flex flex-col items-center text-white bg-cover">
            <h1 className="text-3xl mb-8">
                Emergency Ambulance System
            </h1>
            {!ambulances &&
                <div className="w-3/12 flex flex-col items-center" onClick={() => setAmbulances((ambulances)=>!ambulances)}>
                    <Lottie animationData={waiting} className="w-full h-full"/>
                    <button className="bg-white text-black p-4 text-2xl font-semibold border rounded-lg">
                        Alert Police
                    </button>
                </div>
            }
            {ambulances &&
                Open()
            }
        </div>
    )
}