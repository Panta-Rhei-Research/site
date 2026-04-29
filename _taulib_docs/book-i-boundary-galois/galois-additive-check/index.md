---
{
  "projection_kind": "taulib_declaration",
  "title": "galois_additive_check",
  "permalink": "/verify/taulib/docs/book-i-boundary-galois/galois-additive-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Galois`.",
  "declaration_id": "TauLib.BookI.Boundary.Galois::galois_additive_check",
  "declaration_slug": "galois-additive-check",
  "kind": "def",
  "name": "galois_additive_check",
  "module_name": "TauLib.BookI.Boundary.Galois",
  "module_url": "/verify/taulib/docs/book-i-boundary-galois/",
  "source_line_start": 118,
  "source_line_end": 134,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L118-L134",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Galois",
        "url": "/verify/taulib/docs/book-i-boundary-galois/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L118-L134",
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

- Module: [TauLib.BookI.Boundary.Galois](/verify/taulib/docs/book-i-boundary-galois/)
- Source path: [`TauLib/BookI/Boundary/Galois.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L118-L134)
- Source range: L118-L134
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D95a] Check that σ_a preserves addition: σ(x+y) = σ(x)+σ(y). -/
```

## Source Excerpt

```lean
def galois_additive_check (σ : GaloisAut) : Bool :=
  let pk := primorial σ.stage
  go 0 pk pk
where
  go (x pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else go_inner x 0 pk pk && go (x + 1) pk (fuel - 1)
  termination_by fuel
  go_inner (x y pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if y >= pk then true
    else
      let lhs := galois_apply σ ((x + y) % pk)
      let rhs := (galois_apply σ x + galois_apply σ y) % pk
      (lhs == rhs) && go_inner x (y + 1) pk (fuel - 1)
  termination_by fuel
```
