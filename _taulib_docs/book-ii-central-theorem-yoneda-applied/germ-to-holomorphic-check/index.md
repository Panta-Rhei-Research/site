---
{
  "projection_kind": "taulib_declaration",
  "title": "germ_to_holomorphic_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/germ-to-holomorphic-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.YonedaApplied`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.YonedaApplied::germ_to_holomorphic_check",
  "declaration_slug": "germ-to-holomorphic-check",
  "kind": "def",
  "name": "germ_to_holomorphic_check",
  "module_name": "TauLib.BookII.CentralTheorem.YonedaApplied",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/",
  "source_line_start": 210,
  "source_line_end": 228,
  "registry_ids": [
    "II.T39"
  ],
  "related_registry_items": [
    {
      "id": "II.T39",
      "title": "Omega-Germs iff Holomorphic Functions",
      "url": "/registry/object/II.T39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L210-L228",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.YonedaApplied",
        "url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L210-L228",
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

- Module: [TauLib.BookII.CentralTheorem.YonedaApplied](/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/)
- Source path: [`TauLib/BookII/CentralTheorem/YonedaApplied.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L210-L228)
- Source range: L210-L228
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T39` — Omega-Germs iff Holomorphic Functions

## Immediate Comment / Docstring

```lean
/-- [II.T39] Reverse direction: every omega-germ transformer determines
    a holomorphic function.

    Given the omega-germ data (the tower of reduce values), we reconstruct
    the tower-coherent function via Decode, and verify it is tower-coherent.

    For input table(a) = a (identity table):
    - decode_reconstruct(table, k, x) = table(reduce(x, k)) = reduce(x, k)
    - This IS the identity StageFun, which is tower-coherent.
    - So the omega-germ (encoded as a code table) reconstructs to a holomorphic function. -/
```

## Source Excerpt

```lean
def germ_to_holomorphic_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- Omega-germ data: table(a) = a (identity germ)
      let table : TauIdx -> Int := fun a => (a : Int)
      -- Decode reconstructs: decoded(x, k) = table(reduce(x, k)) = reduce(x, k)
      let decoded_val := decode_reconstruct table k x
      let direct_val : Int := (reduce x k : Int)
      let match_ok := decoded_val == direct_val
      -- Tower coherence of decoded: reduce(decoded(x, k+1), k) = decoded(x, k)
      let decoded_next := decode_reconstruct table (k + 1) x
      let tc_ok := (decoded_next.toNat % primorial k : Int) == decoded_val % (primorial k : Int)
      match_ok && tc_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
