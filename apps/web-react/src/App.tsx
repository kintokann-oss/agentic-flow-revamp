import { useEffect, useState } from 'react'
import { useTranslation } from 'react-i18next'
import { fetchInfo, type InfoResponse } from './api/info'
import './App.css'

function App() {
  const { t } = useTranslation('app')
  const [info, setInfo] = useState<InfoResponse | null>(null)
  const [infoError, setInfoError] = useState<string | null>(null)

  useEffect(() => {
    fetchInfo()
      .then(setInfo)
      .catch((err: Error) => setInfoError(err.message))
  }, [])

  return (
    <main className="app-shell" data-testid="app-shell">
      <header className="app-header">
        <h1>{t('title')}</h1>
        {info && (
          <p className="app-version" data-testid="api-info">
            v{info.version}
          </p>
        )}
      </header>

      {infoError && (
        <p className="app-error" role="alert">
          {t('errors.serverUnreachable')}
        </p>
      )}
    </main>
  )
}

export default App
