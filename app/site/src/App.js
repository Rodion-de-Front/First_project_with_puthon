import React from "react"

import Header from "./components/Header"

class App extends React.Component {

  constructor (props) {
    super(props)
    this.state = {
        text: "Help text",
        userData: "",
    }

    // разрешаем функции работать с состояниями
    this.inputClick = this.inputClick.bind(this)

  }

  render () {
    return (
      <div className="name">
        <Header title="Header" />
        <h1>{this.state.text}</h1>
        <h2>{this.state.userData}</h2>
        <input placeholder={this.state.text}  onClick={this.inputClick} onChange={event => this.setState({userData: event.target.value})}/>
        <p>{this.state.text}</p>
      </div>
    )
  }

  inputClick() {
    this.setState({text: "Changed"})
    console.log("clicked")
  }

}

export default App