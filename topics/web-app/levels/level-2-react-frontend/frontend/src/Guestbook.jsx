function Guestbook({ entries }) {
  return (
    <div className="entries">
      <h2>Guestbook Entries</h2>

      {entries.length === 0 ? (
        <p>No entries yet.</p>
      ) : (
        entries.map((entry, index) => (
          <div className="entry" key={index}>
            <h3>{entry.name}</h3>
            <p>{entry.message}</p>
          </div>
        ))
      )}
    </div>
  )
}

export default Guestbook
