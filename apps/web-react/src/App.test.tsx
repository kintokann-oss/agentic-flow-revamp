import { render, screen } from '@testing-library/react'
import { describe, expect, it, vi } from 'vitest'
import App from './App'
import * as infoApi from './api/info'

describe('App', () => {
  it('renders API info when fetch succeeds', async () => {
    vi.spyOn(infoApi, 'fetchInfo').mockResolvedValue({
      name: 'test-project-agentic-flow',
      version: '0.1.0',
    })

    render(<App />)

    expect(await screen.findByTestId('api-info')).toHaveTextContent('v0.1.0')
    expect(screen.getByTestId('app-shell')).toBeInTheDocument()
  })
})
