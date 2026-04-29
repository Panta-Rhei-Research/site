---
{
  "projection_kind": "taulib_declaration",
  "title": "axiom_operation",
  "permalink": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/axiom-operation/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ZFCasVM`.",
  "declaration_id": "TauLib.BookIII.Bridge.ZFCasVM::axiom_operation",
  "declaration_slug": "axiom-operation",
  "kind": "def",
  "name": "axiom_operation",
  "module_name": "TauLib.BookIII.Bridge.ZFCasVM",
  "module_url": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/",
  "source_line_start": 75,
  "source_line_end": 99,
  "registry_ids": [
    "III.D68"
  ],
  "related_registry_items": [
    {
      "id": "III.D68",
      "title": "Gödel Numbering as NF Address",
      "url": "/registry/object/III.D68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L75-L99",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ZFCasVM",
        "url": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L75-L99",
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

- Module: [TauLib.BookIII.Bridge.ZFCasVM](/verify/taulib/docs/book-iii-bridge-zfcas-vm/)
- Source path: [`TauLib/BookIII/Bridge/ZFCasVM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L75-L99)
- Source range: L75-L99
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D68` — Gödel Numbering as NF Address

## Immediate Comment / Docstring

```lean
/-- [III.D68] Encoding of a ZFC axiom as a tau-address operation.
    Each axiom maps (a, b) to a result at primorial depth k. -/
```

## Source Excerpt

```lean
def axiom_operation (ax : ZFCAxiom) (a b k : TauIdx) : TauIdx :=
  let pk := primorial k
  if pk == 0 then 0
  else match ax with
  | .extensionality => -- a ≡ b mod P_k means "same elements at depth k"
    if reduce a k == reduce b k then 1 else 0
  | .pairing => -- {a,b} encoded as (a + b * (P_k / 2)) mod P_k
    let half := pk / 2
    (a + b * half) % pk
  | .union => -- union = sum mod P_k (flatten nested encoding)
    (a + b) % pk
  | .powerset => -- powerset = a^2 mod P_k (exponential growth modeled)
    (a * a) % pk
  | .infinity => -- infinity witness = a + 1 mod P_k (successor always exists)
    (a + 1) % pk
  | .separation => -- filter: keep a if b is nonzero (b = predicate value)
    if b % pk == 0 then 0 else a % pk
  | .replacement => -- image: apply b as function to a (multiplicative, distinct from union)
    (a * (b + 1)) % pk
  | .foundation => -- well-founded: rank of a at depth k (ordinal rank in ∈-chain)
    (a % pk) / 2
  | .choice => -- choice: pick the smaller of a, b mod P_k
    let ar := a % pk
    let br := b % pk
    if ar <= br then ar else br
```
