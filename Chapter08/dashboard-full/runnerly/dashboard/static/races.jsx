var RacesBox = React.createClass( {
    loadRacesFromServer: function()  {
        var xhr = new XMLHttpRequest();
        xhr.open('get', this.props.url, true);
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
        this.loadRacesFromServer();
    } ,

    render: function()  {
        return (
            <div>
                <h2>Races</h2>
                <Races data= {this.state.data}  />
            </div>
      );
    }
} );

var Races = React.createClass( {
    render: function()  {
        var runNodes = this.props.data.map(function (run)  {
            return (
              <Race
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


// Here we decide what goes in a Thing node, which we defined above.
var Race = React.createClass( {
    render: function()  {
        return (
          <div>{this.props.title} ({this.props.type})</div>
      );
    }
} );

