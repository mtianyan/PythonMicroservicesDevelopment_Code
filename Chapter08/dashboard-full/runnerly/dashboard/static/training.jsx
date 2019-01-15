var TrainingRunsBox = React.createClass( {
    loadTrainingRunsFromServer: function()  {
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
        this.loadTrainingRunsFromServer();
    } ,

    render: function()  {
        return (
            <div>
                <h2>TrainingRuns</h2>
                <TrainingRuns data= {this.state.data}  />
            </div>
      );
    }
} );

var TrainingRuns = React.createClass( {
    render: function()  {
        var runNodes = this.props.data.map(function (run)  {
            return (
              <TrainingRun
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
var TrainingRun = React.createClass( {
    render: function()  {
        return (
          <div>{this.props.title} ({this.props.type})</div>
      );
    }
} );

