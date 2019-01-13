ReactDOM.render(
  <RunsBox url="/api/runs.json" />,
  document.getElementById('runs')
);

ReactDOM.render(
  <RacesBox url="/api/races.json" />,
  document.getElementById('races')
);

ReactDOM.render(
  <TrainingRunsBox url="/api/training.json" />,
  document.getElementById('training')
);
