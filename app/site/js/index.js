function inputClick() {
    console.log("clicked")
}

let text = "Help text"

const elements = (
<div className="name">
    <h1>{text}</h1>
    <input placeholder={text} onClick={inputClick}/>
    <p>{text}</p>
</div>
)

ReactDOM.render(elements, document.getElementById("app"))

