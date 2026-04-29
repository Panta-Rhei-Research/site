---
{
  "projection_kind": "taulib_declaration",
  "title": "ontic_closure",
  "permalink": "/verify/taulib/docs/book-i-orbit-closure/ontic-closure/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Closure`.",
  "declaration_id": "TauLib.BookI.Orbit.Closure::ontic_closure",
  "declaration_slug": "ontic-closure",
  "kind": "theorem",
  "name": "ontic_closure",
  "module_name": "TauLib.BookI.Orbit.Closure",
  "module_url": "/verify/taulib/docs/book-i-orbit-closure/",
  "source_line_start": 36,
  "source_line_end": 43,
  "registry_ids": [
    "I.T01"
  ],
  "related_registry_items": [
    {
      "id": "I.T01",
      "title": "Ontic Closure",
      "url": "/registry/object/I.T01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Closure.lean#L36-L43",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Closure",
        "url": "/verify/taulib/docs/book-i-orbit-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Closure.lean#L36-L43",
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

- Module: [TauLib.BookI.Orbit.Closure](/verify/taulib/docs/book-i-orbit-closure/)
- Source path: [`TauLib/BookI/Orbit/Closure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Closure.lean#L36-L43)
- Source range: L36-L43
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T01` — Ontic Closure

## Immediate Comment / Docstring

```lean
/-- [I.T01] Ontic Closure: every TauObj is either in an orbit ray
    or has seed omega. -/
```

## Source Excerpt

```lean
theorem ontic_closure (x : TauObj) :
    (∃ g, g ≠ omega ∧ OrbitRay g x) ∨ x.seed = omega := by
  cases h : x.seed with
  | omega => exact Or.inr rfl
  | alpha => exact Or.inl ⟨alpha, by decide, h, by decide⟩
  | pi => exact Or.inl ⟨pi, by decide, h, by decide⟩
  | gamma => exact Or.inl ⟨gamma, by decide, h, by decide⟩
  | eta => exact Or.inl ⟨eta, by decide, h, by decide⟩
```
