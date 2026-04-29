---
{
  "projection_kind": "taulib_declaration",
  "title": "truth4ToChannel",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/truth4-to-channel/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.H4BoundaryAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.H4BoundaryAlgebra::truth4ToChannel",
  "declaration_slug": "truth4-to-channel",
  "kind": "def",
  "name": "truth4ToChannel",
  "module_name": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/",
  "source_line_start": 254,
  "source_line_end": 265,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L254-L265",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
        "url": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L254-L265",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.Polarity.H4BoundaryAlgebra](/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/)
- Source path: [`TauLib/BookI/Polarity/H4BoundaryAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L254-L265)
- Source range: L254-L265
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §10 dictionary**: bijection between Truth4 atoms and
    channel-eigenstates.  Named `truth4ToChannel` (rather than
    `Truth4.toChannelEigenstate`) to avoid creating a
    `Tau.Polarity.Truth4` namespace that would shadow
    `Tau.Logic.Truth4`. -/
```

## Source Excerpt

```lean
def truth4ToChannel : Truth4 → ChannelEigenstate
  | Truth4.F => ChannelEigenstate.alphaNull   -- F = 0 → α-null
  | Truth4.B => ChannelEigenstate.gammaEM     -- B = e_+ → γ (EM)
  | Truth4.N => ChannelEigenstate.etaStrong   -- N = e_- → η (strong)
  | Truth4.T => ChannelEigenstate.alphaTotal  -- T = 1 → α-total

/-- **The four-atom dictionary as a structural identity**: each
    Truth4 constructor corresponds to a specific physics channel. -/
@[simp] theorem channel_at_F : truth4ToChannel Truth4.F = ChannelEigenstate.alphaNull := rfl
@[simp] theorem channel_at_B : truth4ToChannel Truth4.B = ChannelEigenstate.gammaEM := rfl
@[simp] theorem channel_at_N : truth4ToChannel Truth4.N = ChannelEigenstate.etaStrong := rfl
@[simp] theorem channel_at_T : truth4ToChannel Truth4.T = ChannelEigenstate.alphaTotal := rfl
```
