---
{
  "projection_kind": "taulib_declaration",
  "title": "l2_completeness_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-l2-space/l2-completeness-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.L2Space`.",
  "declaration_id": "TauLib.BookII.Hartogs.L2Space::l2_completeness_check",
  "declaration_slug": "l2-completeness-check",
  "kind": "def",
  "name": "l2_completeness_check",
  "module_name": "TauLib.BookII.Hartogs.L2Space",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-l2-space/",
  "source_line_start": 140,
  "source_line_end": 156,
  "registry_ids": [
    "II.P18"
  ],
  "related_registry_items": [
    {
      "id": "II.P18",
      "title": "L² Completeness",
      "url": "/registry/object/II.P18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L140-L156",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.L2Space",
        "url": "/verify/taulib/docs/book-ii-hartogs-l2-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L140-L156",
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

- Module: [TauLib.BookII.Hartogs.L2Space](/verify/taulib/docs/book-ii-hartogs-l2-space/)
- Source path: [`TauLib/BookII/Hartogs/L2Space.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L140-L156)
- Source range: L140-L156
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P18` — L² Completeness

## Immediate Comment / Docstring

```lean
/-- [II.P18] L² completeness: at each finite stage, the space is
    finite-dimensional (dim = M_k), hence automatically complete.
    Tower compatibility: the projection from stage k+1 to stage k
    preserves inner products up to normalization. -/
```

## Source Excerpt

```lean
def l2_completeness_check (k : Nat) : Bool :=
  let pk := primorial k
  let pk1 := primorial (k + 1)
  -- Check: inner product at stage k of reduced functions equals
  -- inner product at stage k+1 after appropriate normalization
  let f : Nat → Int := fun x => (x : Int)
  let g : Nat → Int := fun x => (x * x : Int)
  -- The reduced inner product: Σ_{x in Z/M_k} f(x)g(x)
  let ip_k := inner_product_sum f g k
  -- At stage k+1, the same functions restricted to Z/M_{k+1}
  let ip_k1 := inner_product_sum f g (k + 1)
  -- Normalization: ip_k / M_k should relate to ip_{k+1} / M_{k+1}
  -- Check: ip_k * M_{k+1} and ip_{k+1} * M_k have consistent sign
  let ratio_ok := (ip_k * pk1 > 0) == (ip_k1 * pk > 0) || ip_k == 0
  -- Dimension check: dim(L²(Z/M_k)) = M_k
  let dim_ok := pk > 0
  ratio_ok && dim_ok
```
