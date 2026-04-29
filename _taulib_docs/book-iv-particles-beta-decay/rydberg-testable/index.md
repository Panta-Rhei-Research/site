---
{
  "projection_kind": "taulib_declaration",
  "title": "rydberg_testable",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/rydberg-testable/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::rydberg_testable",
  "declaration_slug": "rydberg-testable",
  "kind": "def",
  "name": "rydberg_testable",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 221,
  "source_line_end": 222,
  "registry_ids": [
    "IV.R124"
  ],
  "related_registry_items": [
    {
      "id": "IV.R124",
      "title": "A testable prediction",
      "url": "/registry/object/IV.R124/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L221-L222",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.BetaDecay",
        "url": "/verify/taulib/docs/book-iv-particles-beta-decay/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L221-L222",
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

- Module: [TauLib.BookIV.Particles.BetaDecay](/verify/taulib/docs/book-iv-particles-beta-decay/)
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L221-L222)
- Source range: L221-L222
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R124` — A testable prediction

## Immediate Comment / Docstring

```lean
/-- [IV.R124] R_∞ is one of the most precisely measured quantities
    (uncertainty 1.1×10⁻¹²). The τ-prediction matches to 0.026 ppm,
    limited by the m_e residual. -/
```

## Source Excerpt

```lean
def rydberg_testable : String :=
  "R_infinity: CODATA uncertainty 1.1e-12, tau matches to 0.026 ppm (7 sig figs)"
```
