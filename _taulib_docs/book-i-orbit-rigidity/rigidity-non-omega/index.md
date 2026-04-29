---
{
  "projection_kind": "taulib_declaration",
  "title": "rigidity_non_omega",
  "permalink": "/verify/taulib/docs/book-i-orbit-rigidity/rigidity-non-omega/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Rigidity`.",
  "declaration_id": "TauLib.BookI.Orbit.Rigidity::rigidity_non_omega",
  "declaration_slug": "rigidity-non-omega",
  "kind": "theorem",
  "name": "rigidity_non_omega",
  "module_name": "TauLib.BookI.Orbit.Rigidity",
  "module_url": "/verify/taulib/docs/book-i-orbit-rigidity/",
  "source_line_start": 132,
  "source_line_end": 138,
  "registry_ids": [
    "I.T07"
  ],
  "related_registry_items": [
    {
      "id": "I.T07",
      "title": "Rigidity of tau",
      "url": "/registry/object/I.T07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L132-L138",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Rigidity",
        "url": "/verify/taulib/docs/book-i-orbit-rigidity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L132-L138",
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

- Module: [TauLib.BookI.Orbit.Rigidity](/verify/taulib/docs/book-i-orbit-rigidity/)
- Source path: [`TauLib/BookI/Orbit/Rigidity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L132-L138)
- Source range: L132-L138
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T07` — Rigidity of tau

## Immediate Comment / Docstring

```lean
/-- [I.T07] **Rigidity**: φ = id on non-omega objects (given seed preservation). -/
```

## Source Excerpt

```lean
theorem rigidity_non_omega (φ : TauAutomorphism) (g : Generator) (hg : g ≠ omega)
    (h_seed : (φ.toFun ⟨g, 0⟩).seed = g) (n : Nat) :
    φ.toFun ⟨g, n⟩ = ⟨g, n⟩ := by
  have h_shift := auto_shift φ g hg n
  have h_depth := rigidity_depth φ g hg
  rw [h_seed, h_depth] at h_shift
  simpa using h_shift
```
