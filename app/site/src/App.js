import React from "react"

import Header from "./components/Header"
import Users from "./components/Users"
import AddUser from "./components/AddUser"

class App extends React.Component {

  constructor (props) {
    super(props)
    this.state = {
        users: [
            {
                id: 1,
                firstname: 'Bob',
                lastname: 'Marley',
                bio: 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Repell',
                age: 40,
                isHappy: true
            },
            {
                id: 2,
                firstname: 'John',
                lastname: 'Doe',
                bio: 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Repell',
                age: 22,
                isHappy: false

            }
        ]
    }
    this.addUser = this.addUser.bind(this)
  }

  render () {
    return (
      <div className="name">
        <Header title="Список пользователей" />
        <main>
          <Users users={this.state.users}/>
        </main>
        <aside>
          <AddUser onAdd={this.addUser} />
        </aside>
      </div>
    )
  }

  addUser(user) {
    const id = this.state.users.length + 1
    // меняем список users, к текущему списку добавляем нового пользователя
   this.setState({users: [...this.state.users, {id, ...user}]})
  }

}

export default App