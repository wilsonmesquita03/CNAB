import { useEffect } from "react"
import { useState } from "react"
import DetailedShop from "./components/DetailedShop"
import ShopRow from "./components/ShopRow"
import api from "./services"

const App = () => {
    const [shopList, setShopList] = useState([])

    const handleSubmit = (e) => {
        const file = e.target.files[0]
        const res = api.post("cnab/", file, {
            headers: {
                "Content-Type": "*/*"
            }
        })

        console.log(res)
    }

    useEffect(() => {
        const use = async () => {
            try {
                const { data } = await api.get("shops/")
                setShopList(data)
            } catch (error) {
                // Show toast
            }
        }
        use()
    }, [shopList])

    return (
        <div>
            <div>
                <label htmlFor="file">Carregue um arquivo</label>
                <input type="file" id="file" name="file" accept=".txt" onChange={(e) => handleSubmit(e)}/>
            </div>
        </div>
    )
}

export default App