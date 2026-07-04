import { useEffect, useState } from 'react'
import Guestbook from './Guestbook'
import EntryForm from './EntryForm'
import './App.css'

function App() {
  const [entries, setEntries] = useState([])

  useEffect(() => {
    fetch('http://localhost:5000/api/entries')
      .then((response) => response.json())
      .then((data) => setEntries(data))
      .catch((error) => console.error('Error fetching entries:', error))
  }, [])

  const handleEntryAdded = (newEntry) => {
    setEntries((currentEntries) => [...currentEntries, newEntry])
  }

  return (
    <main className="container">
      <h1>React Guestbook</h1>
      <Guestbook entries={entries} />
      <EntryForm onEntryAdded={handleEntryAdded} />
    </main>
  )
}

export default App
