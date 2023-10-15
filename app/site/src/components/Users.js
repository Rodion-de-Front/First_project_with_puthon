import React from "react"
import User from "./User"

class Users extends React.Component {

    render () {
      return (
        <div>
            {this.props.users.map((el) => (
                <User key={el.id} user={el} />
            ))}
        </div>
      )
    }

}

export default Users