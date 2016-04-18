var TodoItem = React.createClass({
  render: function() {
      return  <li>{this.props.item.text} </li>;
  }
});

var TodoList = React.createClass({
  render: function() {
	  var todos = this.props.items.map(function(item) {
      return (
				<TodoItem item={item} />
      );
    });
    return  <ul>{todos}</ul>;
  }
});

var TodoApp = React.createClass({
  getInitialState: function() {
    return {
    	items: [{text: 'Eat'}, {text: 'Study'}, {text: 'Sleep'}],
      text: ''
    };
  },

  onChange: function(e){
    this.setState({
      text: e.target.value
    });
  },

	handleSubmit: function(e) {
  	e.preventDefault();
    var nextItems = this.state.items.concat([{
    	text: this.state.text,
    }]);

    this.setState({
    	items: nextItems,
      text: ''
    });
  },

  render: function() {
    return (
      <div>
        <h3>TODO</h3>
        <TodoList items={this.state.items} />

        <form onSubmit={this.handleSubmit}>
          <input onChange={this.onChange} value={this.state.text} />
          <button>{'Add #' + (this.state.items.length + 1)}</button>
        </form>
      </div>
    );
  }
});

ReactDOM.render(<TodoApp />, document.getElementById('container'));
