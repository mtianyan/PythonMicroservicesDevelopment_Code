var RunsBox = React.createClass( {
  loadRunsFromServer: function()  {
    var xhr = new XMLHttpRequest();
    xhr.open('get', this.props.url, true);
    xhr.withCredentials = true;
    xhr.onload = function()  {
      var data = JSON.parse(xhr.responseText);
      this.setState( { data: data } );
    } .bind(this);
    xhr.send();
  } ,

  getInitialState: function()  {
    return  {data: []} ;
  } ,

  componentDidMount: function()  {
    this.loadRunsFromServer();
  } ,

  render: function()  {
    return (
      <div>
        <h2>Runs</h2>
        <Runs data= {this.state.data}  />
      </div>
    );
  }
} );

var Runs = React.createClass( {
  render: function()  {
    var runNodes = this.props.data.map(function (run)  {
      return (
        <Run
          title= {run.title}
          type= {run.type}
        />
      );
    } );

    return (
      <div>
        {runNodes}
      </div>
    );
  }
} );


var Run = React.createClass( {
  render: function()  {
    return (
      <div>{this.props.title} ({this.props.type})</div>
    );
  }
} );


window.RunsBox = RunsBox;
