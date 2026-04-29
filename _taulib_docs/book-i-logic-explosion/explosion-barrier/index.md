---
{
  "projection_kind": "taulib_declaration",
  "title": "explosion_barrier",
  "permalink": "/verify/taulib/docs/book-i-logic-explosion/explosion-barrier/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Logic.Explosion`.",
  "declaration_id": "TauLib.BookI.Logic.Explosion::explosion_barrier",
  "declaration_slug": "explosion-barrier",
  "kind": "theorem",
  "name": "explosion_barrier",
  "module_name": "TauLib.BookI.Logic.Explosion",
  "module_url": "/verify/taulib/docs/book-i-logic-explosion/",
  "source_line_start": 51,
  "source_line_end": 52,
  "registry_ids": [
    "I.T13"
  ],
  "related_registry_items": [
    {
      "id": "I.T13",
      "title": "Explosion Barrier",
      "url": "/registry/object/I.T13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Explosion.lean#L51-L52",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Logic.Explosion",
        "url": "/verify/taulib/docs/book-i-logic-explosion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Explosion.lean#L51-L52",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Logic.Explosion](/verify/taulib/docs/book-i-logic-explosion/)
- Source path: [`TauLib/BookI/Logic/Explosion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Explosion.lean#L51-L52)
- Source range: L51-L52
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T13` — Explosion Barrier

## Immediate Comment / Docstring

```lean
/-- [I.T13] The explosion barrier: B does not imply everything.
    Specifically, impl B F = N, not T.
    This is the central paraconsistent feature of Truth4.

    Calculation: impl B F = join (neg B) F = join N F = N.
    Since N <> T, the implication B -> F is not "true". -/
```

## Source Excerpt

```lean
theorem explosion_barrier : Truth4.impl B F ≠ T := by
  simp [Truth4.impl, Truth4.neg, Truth4.join]
```
