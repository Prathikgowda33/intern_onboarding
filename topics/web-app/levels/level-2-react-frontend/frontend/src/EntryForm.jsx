import { useState } from 'react'

function EntryForm({ onEntryAdded }) {
  const [name, setName] = useState('')
  const [message, setMessage] = useState('')

  const handleSubmit = async (event) => {
    event.preventDefault()

    const response = await fetch('http://localhost:5000/api/entries', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, message }),
    })

    if (response.ok) {
      const newEntry = await response.json()
      onEntryAdded(newEntry)
      setName('')
      setMessage('')
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Entry</h2>

      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={(event) => setName(event.target.value)}
        required
      />

      <textarea
        placeholder="Message"
        value={message}
        onChange={(event) => setMessage(event.target.value)}
        required
      />

      <button type="submit">Add Entry</button>
    </form>
  )
}

export default EntryForm
