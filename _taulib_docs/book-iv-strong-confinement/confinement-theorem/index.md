---
{
  "projection_kind": "taulib_declaration",
  "title": "ConfinementTheorem",
  "permalink": "/verify/taulib/docs/book-iv-strong-confinement/confinement-theorem/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.Confinement`.",
  "declaration_id": "TauLib.BookIV.Strong.Confinement::ConfinementTheorem",
  "declaration_slug": "confinement-theorem",
  "kind": "structure",
  "name": "ConfinementTheorem",
  "module_name": "TauLib.BookIV.Strong.Confinement",
  "module_url": "/verify/taulib/docs/book-iv-strong-confinement/",
  "source_line_start": 101,
  "source_line_end": 110,
  "registry_ids": [
    "IV.T71"
  ],
  "related_registry_items": [
    {
      "id": "IV.T71",
      "title": "Confinement Theorem",
      "url": "/registry/object/IV.T71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L101-L110",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.Confinement",
        "url": "/verify/taulib/docs/book-iv-strong-confinement/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L101-L110",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Strong.Confinement](/verify/taulib/docs/book-iv-strong-confinement/)
- Source path: [`TauLib/BookIV/Strong/Confinement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L101-L110)
- Source range: L101-L110
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T71` — Confinement Theorem

## Immediate Comment / Docstring

```lean
/-- [IV.T71] Confinement Theorem: no isolated color-charged state
    resolves to a stable element of H_partial[omega].

    The boundary character sequence for a mode with exp(2pi i c/3)
    holonomy (c != 0 mod 3) fails to converge because the fractional
    eta-phase prevents cancellation in the profinite limit.

    This is NOT an input or assumption — it follows from the boundary
    holonomy algebra structure at depth 3 with chi_minus dominance. -/
```

## Source Excerpt

```lean
structure ConfinementTheorem where
  /-- Isolated color-charged states do not exist at omega. -/
  no_isolated_colored : Bool := true
  /-- Mechanism: non-convergence of fractional holonomy. -/
  mechanism : String := "fractional eta-phase prevents profinite convergence"
  /-- Scope: tau-effective (derived, not assumed). -/
  scope : String := "tau-effective"
  /-- Source: boundary holonomy at depth 3 with chi_minus dominance. -/
  source : String := "depth-3 chi_minus-dominant boundary holonomy"
  deriving Repr
```
