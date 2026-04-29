---
{
  "projection_kind": "taulib_declaration",
  "title": "make_proto_code",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/make-proto-code/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.ProtoCodes`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ProtoCodes::make_proto_code",
  "declaration_slug": "make-proto-code",
  "kind": "def",
  "name": "make_proto_code",
  "module_name": "TauLib.BookIII.Arithmetic.ProtoCodes",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/",
  "source_line_start": 50,
  "source_line_end": 59,
  "registry_ids": [
    "III.D61"
  ],
  "related_registry_items": [
    {
      "id": "III.D61",
      "title": "Proto-Code",
      "url": "/registry/object/III.D61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L50-L59",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ProtoCodes",
        "url": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L50-L59",
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

- Module: [TauLib.BookIII.Arithmetic.ProtoCodes](/verify/taulib/docs/book-iii-arithmetic-proto-codes/)
- Source path: [`TauLib/BookIII/Arithmetic/ProtoCodes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L50-L59)
- Source range: L50-L59
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D61` — Proto-Code

## Immediate Comment / Docstring

```lean
/-- [III.D61] Construct a proto-code from address and depth. -/
```

## Source Excerpt

```lean
def make_proto_code (x k : TauIdx) : ProtoCode :=
  let pk := primorial k
  if pk == 0 then ⟨0, k, 0, true⟩
  else
    let xr := x % pk
    let nf := boundary_normal_form xr k
    let sum := (nf.b_part + nf.c_part + nf.x_part) % pk
    let r := rank_as_depth x k
    -- Verified: BNF recovers input AND non-zero addresses have non-zero components
    ⟨xr, k, r, sum == xr && (xr == 0 || nf.b_part > 0 || nf.c_part > 0 || nf.x_part > 0)⟩
```
