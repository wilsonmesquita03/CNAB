const ShopRow = ({shopName, balance}) => {
    return (
        <tr>
            <th>{shopName}</th>
            <td>{balance}</td>
        </tr>
    )
}

export default ShopRow