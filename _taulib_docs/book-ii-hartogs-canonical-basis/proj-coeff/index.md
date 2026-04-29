---
{
  "projection_kind": "taulib_declaration",
  "title": "proj_coeff",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/proj-coeff/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CanonicalBasis`.",
  "declaration_id": "TauLib.BookII.Hartogs.CanonicalBasis::proj_coeff",
  "declaration_slug": "proj-coeff",
  "kind": "def",
  "name": "proj_coeff",
  "module_name": "TauLib.BookII.Hartogs.CanonicalBasis",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/",
  "source_line_start": 230,
  "source_line_end": 239,
  "registry_ids": [
    "II.P09"
  ],
  "related_registry_items": [
    {
      "id": "II.P09",
      "title": "Decomposition Functoriality",
      "url": "/registry/object/II.P09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L230-L239",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CanonicalBasis",
        "url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L230-L239",
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

- Module: [TauLib.BookII.Hartogs.CanonicalBasis](/verify/taulib/docs/book-ii-hartogs-canonical-basis/)
- Source path: [`TauLib/BookII/Hartogs/CanonicalBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L230-L239)
- Source range: L230-L239
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P09` — Decomposition Functoriality

## Immediate Comment / Docstring

```lean
/-- [II.P09] Spectral projection coefficient:
    proj_coeff(f, k, prime_idx, v) = sum over x in Z/P_kZ of f(x) * E_{k,p,v}(x). -/
```

## Source Excerpt

```lean
def proj_coeff (f : TauIdx → Int) (k prime_idx v : TauIdx) : Int :=
  go 0 (primorial k) (0 : Int)
where
  go (x fuel : Nat) (acc : Int) : Int :=
    if fuel = 0 then acc
    else if x >= primorial k then acc
    else
      let g := cylinder_gen k prime_idx v true x
      go (x + 1) (fuel - 1) (acc + f x * g)
  termination_by fuel
```
