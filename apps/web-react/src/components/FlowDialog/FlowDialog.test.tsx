import { render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import i18n from '../../i18n'
import { FlowDialog } from './FlowDialog'

describe('FlowDialog', () => {
  it('shows off when flow is false', () => {
    render(<FlowDialog flowActive={false} />)
    expect(screen.getByTestId('flow-dialog')).toHaveClass('flow-dialog--idle')
    expect(screen.getByText(i18n.t('app:flow.off'))).toBeInTheDocument()
  })

  it('shows on when flow is true', () => {
    render(<FlowDialog flowActive={true} />)
    expect(screen.getByTestId('flow-dialog')).toHaveClass('flow-dialog--active')
    expect(screen.getByText(i18n.t('app:flow.on'))).toBeInTheDocument()
  })
})
