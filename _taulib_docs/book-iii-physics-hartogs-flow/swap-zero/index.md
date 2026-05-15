---
{
  "projection_kind": "taulib_declaration",
  "title": "swap_zero",
  "permalink": "/corpus/taulib/docs/book-iii-physics-hartogs-flow/swap-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.HartogsFlow`.",
  "declaration_id": "TauLib.BookIII.Physics.HartogsFlow::swap_zero",
  "declaration_slug": "swap-zero",
  "kind": "theorem",
  "name": "swap_zero",
  "module_name": "TauLib.BookIII.Physics.HartogsFlow",
  "module_url": "/corpus/taulib/docs/book-iii-physics-hartogs-flow/",
  "source_line_start": 229,
  "source_line_end": 230,
  "registry_ids": [
    "III.D41"
  ],
  "related_registry_items": [
    {
      "id": "III.D41",
      "title": "Operator Polarity Swap",
      "url": "/registry/object/III.D41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L229-L230",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.HartogsFlow",
        "url": "/corpus/taulib/docs/book-iii-physics-hartogs-flow/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L229-L230",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIII.Physics.HartogsFlow](/corpus/taulib/docs/book-iii-physics-hartogs-flow/)
- Source path: [`TauLib/BookIII/Physics/HartogsFlow.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L229-L230)
- Source range: L229-L230
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D41` — Operator Polarity Swap

## Immediate Comment / Docstring

```lean
/-- [III.D41] Structural: polarity swap of zero is zero. -/
```

## Source Excerpt

```lean
theorem swap_zero :
    polarity_swap ⟨0, 0, 0, 3⟩ = ⟨0, 0, 0, 3⟩ := rfl
```
